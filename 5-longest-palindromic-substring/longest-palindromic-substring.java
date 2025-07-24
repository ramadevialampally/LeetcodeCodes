class Solution {
    public String longestPalindrome(String s) {
        int reslen=0;
        String res="";
        for(int  i=0;i<s.length();i++){
            int st=i;
            int e=i;
            while(st>=0 && e<s.length() && s.charAt(st)==s.charAt(e)){
                if((e-st+1)>reslen){
                    res=s.substring(st,e+1);
                    reslen=e-st+1;
                }
                st-=1;
                e+=1;
            }
            st=i;
            e=i+1;
            while(st>=0 && e<s.length() && s.charAt(st)==s.charAt(e)){
                if((e-st+1)>reslen){
                    res=s.substring(st,e+1);
                    reslen=e-st+1;
                }
                st-=1;
                e+=1;
            }
        }
        return res;
    }
}