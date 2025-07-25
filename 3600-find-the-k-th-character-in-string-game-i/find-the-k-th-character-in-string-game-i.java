class Solution {
   String character(String ans,int k){
    if(ans.length()>=k){
        return ans;

    }
    StringBuilder tem=new StringBuilder();
    tem.append(ans);
    for(int i=0;i<ans.length();i++){
        tem.append((char)(ans.charAt(i)+1));
    }
    return character(tem.toString(),k);
   }
    public char kthCharacter(int k) {
        String ans="a";
        String res=character(ans,k);
        System.out.println(res);
        return res.charAt(k-1);

        
    }
}