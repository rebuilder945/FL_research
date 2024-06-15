class TestCasesNotIncludedError(Exception):
    def __init__(self,):
        super().__init__()
    
    def __str__(self) -> str:        
        return "TestCasesNotIncludedError: test cases for this porblem is not included yet"

class FaultLocalizationError(Exception):
    def __init__(self, target_lines, total_code_line):
        super().__init__()
        self.target_lines = target_lines
        self.total_code_line = total_code_line
    
    def __str__(self) -> str:        
        return "FaultLocalizationError: Fault localization failed"
    
class FormatError(Exception):
    def __init__(self, info):
        super().__init__()
        self.info = info
    
    def __str__(self) -> str:        
        return "FormatError: print in incorrect format"

class ProbNotIncludedError(Exception):
    def __init__(self,):
        super().__init__()
    
    def __str__(self) -> str:        
        return "ProbNotIncludedError: this problem is not included in the dataset yet"

class TimeoutException(Exception):
    def __init__(self,):
        super().__init__()
    
    def __str__(self) -> str:        
        return "TimeOutError: this code runs too long"

class MutationFailedError(Exception):
    def __init__(self,):
        super().__init__()
    
    def __str__(self) -> str:
        return "MutationFailedError: 可能原因：1）变异体文件全部构造失败；2）变异体全部变编译不通过；3）变异体规则生成失败。"