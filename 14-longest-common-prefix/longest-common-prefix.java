class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder res=new StringBuilder();
        int minlen=Integer.MAX_VALUE;
        for(int i=0;i<strs.length;i++){
            if(strs[i].length()<minlen){
                minlen=strs[i].length();
            }
        }
        for(int i=0;i<minlen;i++){
            char c=strs[0].charAt(i);
            boolean flag=true;
            for(int j=0;j<strs.length-1;j++){
                if(strs[j].charAt(i)!=strs[j+1].charAt(i)){
                    flag=false;
                    break;
                }

            }
            if(flag){
                res.append(c);
            }
            else{
                break;
            }
            
        }
        return res.toString();
        
    }
}