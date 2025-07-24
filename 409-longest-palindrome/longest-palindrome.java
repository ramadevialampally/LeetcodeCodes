class Solution {
    public int longestPalindrome(String s) {
        Set<Character> a=new HashSet<>();
        for(int i=0;i<s.length();i++){
            if(! a.contains(s.charAt(i))){
                a.add(s.charAt(i));
            }
            else{
                a.remove(s.charAt(i));
            }

        }
        if(a.size()!=0){
            return s.length()-a.size()+1;
        }
        return s.length();
        
    }
}