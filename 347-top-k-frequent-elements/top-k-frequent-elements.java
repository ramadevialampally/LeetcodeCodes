class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            h.put(nums[i],h.getOrDefault(nums[i],0)+1);
        }
        
        List<Map.Entry<Integer,Integer>> li=new ArrayList<>(h.entrySet());
        li.sort((a,b)->b.getValue().compareTo(a.getValue()));
        int[] res=new int[k];
        int j=0;
        for(Map.Entry<Integer,Integer> entry:li){
            if(k==0){
                break;
            }
            res[j]=entry.getKey();
            j+=1;
            k-=1;
        }
        return res;
        
        
    }
}