class Solution {
    HashSet<String> res=new HashSet<>();
    void digi(int[] digits,boolean[]used,String cs){
        if(cs.length()==3){
            if(cs.charAt(0)!='0' && (cs.charAt(2)-'0')%2==0){
                res.add(cs);
            }
            return;
        }
        for(int i=0;i<digits.length;i++){
            if(!used[i]){
                used[i]=true;
                digi(digits,used,cs+digits[i]);
                used[i]=false;
            }
        }

    }
    public int totalNumbers(int[] digits) {
        int count=0;
        String cs="";
        res.clear();
        boolean[] used=new boolean[digits.length];
        digi(digits,used,cs);
        return res.size();
        
    }
}