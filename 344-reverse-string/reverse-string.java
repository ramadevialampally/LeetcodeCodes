class Solution {
    public void reverseString(char[] s) {
        int i=0,e=s.length-1;
        while(i<e){
            char t=s[i];
            s[i]=s[e];
            s[e]=t;
            i+=1;
            e-=1;
        }
        
    }
}