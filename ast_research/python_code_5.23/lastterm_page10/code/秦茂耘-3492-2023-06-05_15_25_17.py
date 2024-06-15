#include <iostream>
#include <map>
#include <algorithm>
#include <list>

using namespace std;
char findFirstCh(string str){
       list<char> store;//存储只出现一次的字符
       list<char> storeDel;//存储重复出现的字符
       for(unsigned int i = 0; i < str.size(); ++i){
               list<char>::iterator litor = find(store.begin(), store.end(), str[i]);//查找list里是否已经存在当前字符
               list<char>::iterator litorDel = find(storeDel.begin(), storeDel.end(), str[i]);//还要查找已经出现过的重复字符
               if(litor != store.end()){//如果存在，说明该字符在字符串里是重复的，把字符从list里删除
                       store.remove(str[i]);
                       if(litorDel == storeDel.end()){//记录重复的字符
                            storeDel.push_back(str[i]);
                       }
               }
               else{//list不存在该字符，当前字符暂时符合要求
                       if(litorDel == storeDel.end())//重复的字符里没有当前字符，符合要求，存入store                       
                            store.push_back(str[i]);               
               }       
       }

       char ch = -1;
       list<char>::iterator it = store.begin();
       if(it != store.end()){//如果list的第一个元素存在，就是我们要找的字符
               ch = *it;
               return ch;
       }
       return -1;//不存在，返回-1
}

int main() {
        string s = "bbccdfeesbsbdfh1h";
        string s1 = "ababcdefghscdfe";
        char ch = findFirstCh(s1);
        if(ch != -1)
            cout << ch <<endl;
        else
            cout << "not match character" << endl;
}
