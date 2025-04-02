class Solution:
    def decodeString(self, s: str) -> str:
        
        st=[]
        res=""
        for i in s:
            if i==']':
                r=""
                
                while st and st[-1]!='[':
                    r=st.pop()+r
                st.pop()
                num=""
                while st and st[-1].isdigit():
                    num = st.pop() + num  
                k=r*int(num)
                st.append(k)
                print(st)
                
                
            else:
                if st and st[-1].isdigit() and i.isdigit():
                    v=st.pop()
                    k=v+i
                    st.append(k)
                else:
                    st.append(i)

        return "".join(st)