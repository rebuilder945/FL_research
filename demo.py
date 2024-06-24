import os
import sys
wk_dir = pk_path = os.path.dirname(__file__)
sys.path.append(pk_path)
os.chdir(wk_dir)
import signal
import sbfl.base
import traceback
import gradio as gr
from coverage import Coverage
from implement.exceptions import *
from implement.utils import *
from implement.techs import FaultLoalization, SBFL, MBFL

init_message = \
"""
    欢迎您使用程序调试机器人!🤗
    该机器人可辅助您理解Python编程作业中出现的错误。机器人基于AI技术，其**回复可能不准确**，仅供您参考。对于机器人的回复，您可以点击按钮进行复制或反馈我们的回复信息是否有帮助。当点击👎时还可输入更详细的反馈信息。您的反馈对我们改善机器人的表现非常重要！
    请在以下第一个对话框中复制作业题目描述，第二个对话框输入存在错误的程序代码，输入回车或点击提交按钮可获得机器人的回复。若要在对话框中输入回车符，请按下**Shift+回车符**
    备注：目前暂**不支持程序片段题（填空题）**
"""


# 前端处理函数
def login(x, y):    
    users = student()
    for username, password in users:
        if username == x and password == y:
            
            return x, y

def print_like_dislike(x: gr.LikeData, history, req: gr.Request):
    dialogue = {
        'input: ': history[x.index[0]][0],
        'response: ': history[x.index[0]][1]
    }

    logger['msg_type'] = 'USER_ATTITUDE'
    logger['is_like'] = x.liked
    logger['dialogue'] = dialogue
    logger.info(req)

    if not x.liked:
        gr.Info('感谢您的反馈，如果能在下方提供宝贵的意见，将不胜感激！')
        return gr.Column(visible=True)
    else:
        gr.Info('感谢您的喜欢！')
        return gr.Column(visible=False)

def submit_feedback(feedback_text, req: gr.Request):
    logger['msg_type'] = 'USER_FEEDBACK'
    logger['feedback'] = feedback_text
    logger.info(req)

    gr.Info('反馈已提交！')
    return gr.Column(visible=False)

def reject_feedback():
    return gr.Column(visible=False)

def alg_set(alg_selected):
    if alg_selected == 'SBFL':
        Fl_app.set_algorithm(algorithm=alg_sbfl)
    else:
        Fl_app.set_algorithm(algorithm=alg_mbfl)

# 算法接口
def respond(message, prob_txt, chat_history, req: gr.Request):

    logger['code_input'] = message
    logger['prob_input'] = prob_txt
    logger['msg_type'] = 'EXCEPTION'

    ans = ""
    prob_id = ""
    debug_info = gr.DataFrame(value=None)

    # front-end exception process
    if message == '':
        gr.Warning('请输入代码')
        return chat_history, debug_info
    if prob_txt == '':
        gr.Warning('请输入问题题目')
        return chat_history, debug_info

    try:
        # 处理逻辑错误
        prob_id = prob2ider.problem_text2id(prob_txt)
        logger['prob_id'] = prob_id
        if prob_id == 0:
            gr.Warning('该问题为程序片段编程题，目前仅支持编程题')
            return chat_history, debug_info

        # 判断input()是否加了参数，则直接返回
        if check_input_args(message):
            ans = "在你的代码中使用了input()函数，由于判题系统的规则，请不要在input()函数中加入任何参数。"
        else:
            # FL分析
            res = Fl_app.get_res(code_=message, prob_id=prob_id, stu=prob_id) # (y, line_rank, outputs_info, target_lines)
            # 格式化为给用户看的输出
            ans = get_target_lines_span(res[-1])                
            ans = f"所提交代码存在**逻辑错误**，错误可能来源于以下**代码行**：\n\n```ss\n{ans}\n"
            alg_text = Fl_app.get_algorithm().text
            debug_info = gr.DataFrame(
                headers=Fl_app.headers[alg_text],
                value=[analysis_res_format(res, alg_text)],
                datatype='markdown',                
            )
            # '\n'.join(analysis_res_format(res, Fl_app.algorithm.text))

            logger['msg_type'] = 'LOGIC_ERROR'
            logger['fix_suggestion'] = str(res)
            logger.info(req)                    
    except FaultLocalizationError as fl_e:
        # 逻辑错误定位失败（所有代码行都被定位）
        ans = "所提交代码存在**逻辑错误**，但很抱歉，我们未能定位错误所在位置。请向助教或老师寻求指导"

        logger['err_info'] = str(fl_e)
        logger['traceback_info'] = traceback.format_exc()

        logger.error(req, {'target_lines': str(fl_e.target_lines), 'total_code_line: ': str(fl_e.total_code_line)})
    except ProbNotIncludedError as pni_e:
        # 题目未导入
        gr.Warning('该题目尚未导入')

        logger['err_info'] = str(pni_e)
        logger['traceback_info'] = traceback.format_exc()
        logger.error(req)
    except TestCasesNotIncludedError as tcnt_e:
        # 题目测试用例未导入
        gr.Warning('该题目测试用例尚未导入')

        logger['err_info'] = str(tcnt_e)
        logger['traceback_info'] = traceback.format_exc()
        logger.error(req)
    except sbfl.base.NoFailingTestError:
        # 完全正确代码错误处理
        gr.Warning('所提交代码已完全正确...')

        logger['err_info'] = 'NoFailingTestError'
        logger['traceback_info'] = traceback.format_exc()
        logger.error(req)
    except MutationFailedError as m_e:
        # 变异测试失败
        ans = "所提交代码进行**变异测试失败**，可能原因：\
                1）变异体全部编译错误； \
                2）变异体文件全部构造失败； \
                2）变异体规则构造失败。"

        logger['err_info'] = str(m_e)
        logger['traceback_info'] = traceback.format_exc()
        logger.error(req)
    except TimeoutException as t_e:
        # 用户提交代码超时
        ans = '所提交代码存在**死循环**，请仔细检查循环条件'

        logger['err_info'] = str(t_e)
        logger['traceback_info'] = traceback.format_exc()
        logger.error(req)
    except FormatError as f_e:
        # 仅仅格式问题直接返回提示
        ans = f_e.info

        logger['err_info'] = str(f_e)
        logger['traceback_info'] = traceback.format_exc()
        logger.error(req)
    except Exception:
        # 编译错误
        stk_info = traceback.format_exc()
        err_info = stk_info.strip().split('\n')[-1]
        res = map_(input_text=err_info)
        ans = str(
                '所提交代码存在**编译错误**，修复建议如下：\n\n' + 
                f'**报错信息**:\n{err_info}\n\n' + 
                res
            )

        logger['msg_type'] = 'COMPILE_ERROR'
        logger['fix_suggestion'] = res
        logger['traceback_info'] = traceback.format_exc()
        logger.info(req)
    finally:
        if ans:
            chat_history.append((message, ans))
        # sys.stdout = sys.__stdout__ # 在FL.alg中已经恢复
        # logger.clear_meta_data()
        return chat_history, debug_info


if __name__ == "__main__":

    # configure params
    switch = 0 # dev: 0; test: 1
    log_file_name = server_port = 0
    server_name = '10.242.187.27'
    # server_name = '127.0.0.1'

    if switch == 0:
        log_file_name =  'tmp/logs/log_dev'
        server_port = 83
    else:
        log_file_name = 'tmp/logs/log_test'
        server_port = 82

    test_cases_folder_path = 'static/data/testcase'   
    prob2id_folder = 'static/prob2id_map'

    # initialize classes
    alg_mbfl = MBFL(cov=Coverage(), my_stdout=CustomStdout(sys.__stdout__), text='mbfl')
    alg_sbfl = SBFL(cov=Coverage(), my_stdout=CustomStdout(sys.__stdout__), text='sbfl')

    session_manager = SessionManager()
    logger = Mylogger(session_manager, log_file_name)
    prob2ider = ProbIdTransformer(prob2id_folder)
    test_cases = TestCasesLoader(test_cases_folder_path).get_test_cases()

    Fl_app = FaultLoalization(
        test_cases=test_cases, 
        logger=logger, 
        algorithm=alg_sbfl
    )

    # layout
    with gr.Blocks() as demo:
        demo.title = '程序调试机器人'
        gr.HTML("""<h1 align="center">程序调试机器人</h1>""")
        user_info_block = gr.Markdown(value="User not logged in")        

        with gr.Row(variant='panel'):

            # placeholder
            with gr.Column(scale=2, variant='panel', visible=True, min_width=0):
                gr.Markdown("### 算法公式")
                gr.Markdown(
                    value="""
            #### MBFL
            $$
            S(m_i) = \\frac{f(m_i)}{\\sqrt{tf(f(m_i) + p(m_i))}}
            $$
            - f(mi): ori未通过而mut_i通过的测试数
            - p(mi): ori通过而mut_i未通过的测试数
            - tf: ori未通过的测试总数

            #### SBFL
            $$
            S(l_i) = \\frac{e_f}{\\sqrt{(e_f+n_f)·(e_f+e_p)}}
            $$
            - ef: 覆盖该行的未通过测试数量
            - ep: 覆盖该行的通过测试数量
            - nf: 未覆盖该行的未通过测试数量
            - ep: 未覆盖该行的通过测试数量
            """,
                    latex_delimiters=[{"left": "$$", "right": "$$", "display": True}],
                )

            with gr.Column(scale=8, variant='panel'):
                with gr.Row():
                    # main body
                    with gr.Column(scale=8, variant='panel'):

                        # dialogue block
                        chatbot = gr.Chatbot(
                                [[None,init_message]],
                                # scale=4,
                                label="对话框",
                                bubble_full_width=False,
                                show_copy_button=True,
                                height="350px",                        
                            )

                        with gr.Row(equal_height=True):

                            # feedback block
                            with gr.Column(scale=2, variant='panel', visible=False) as fb_block:
                                with gr.Column(scale=1):
                                    gr.HTML("""<h2 align="left">提交反馈</h2>""")
                                with gr.Column(scale=3):
                                    feedback = gr.Textbox(  
                                        scale=4,
                                        show_label=False,
                                        placeholder="注意到您不喜欢这个回答，可以在此输入您的反馈建议帮助我们改进吗？",
                                        lines=4,
                                        autofocus=True
                                    )
                                    with gr.Row():
                                        fb_btn = gr.Button("确定", min_width=0)
                                        rejbtn = gr.Button('取消', min_width=0)

                            # input block
                            with gr.Column(scale=4, variant='panel'):

                                # problem snippet
                                prob_txt = gr.Textbox(  
                                    value='读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。',      
                                    label="程序题目", 
                                    placeholder="请在此复制程序题目的内容",
                                    lines=1,
                                    max_lines=1,
                                )

                                # problem content
                                msg = gr.Textbox(            
                                    label='错误代码',
                                    placeholder="请在此复制存在错误的程序源代码",
                                    lines=1,
                                    max_lines=2,
                                ) 
                    # alg select
                    with gr.Column(scale=2, variant='panel'):    
                        alg_selected = gr.Dropdown(
                                                    ["MBFL", "SBFL"],
                                                    value="SBFL",
                                                    label="算法",
                                                    info="请选择错误定位算法",
                                                )

                        submit_btn = gr.Button("提交", min_width=0)
                        clear = gr.ClearButton([msg, chatbot], value='清空对话', min_width=0)

                # debug info                
                debug_info = gr.Dataframe()

            # placeholder
            # with gr.Column(scale=1, visible=True, min_width=0):
            #     gr.HTML(value="<h3></h3>")

        # Events listeners
        # once demo loaded, get session info and keep user info
        demo.load(session_manager.get_user, inputs=None, outputs=[user_info_block])

        # chatbot
        chatbot.like(print_like_dislike, inputs=chatbot, outputs=[fb_block])

        # feedback
        fb_btn.click(submit_feedback, [feedback], [fb_block])
        rejbtn.click(reject_feedback, [], [fb_block])

        # code
        msg.submit(respond, [msg, prob_txt, chatbot], [chatbot, debug_info])
        prob_txt.submit(respond, [msg, prob_txt, chatbot], [chatbot, debug_info])
        submit_btn.click(respond, [msg, prob_txt, chatbot], [chatbot, debug_info])

        # alg select
        alg_selected.change(alg_set, [alg_selected], [])

    demo.launch(
        # auth=login if switch == 1 else None, 
        server_name=server_name, 
        server_port=server_port,
        debug=True
        # prevent_thread_lock=True
    )
