class Solution {
    public List<String> summaryRanges(int[] a) {
        List <String> al=new ArrayList<>();
        for(int i=0;i<a.length;i++){
            int s=a[i];
            while(i+1<a.length && a[i]+1==a[i+1]){
                i++;
            }
            if (s!=a[i]){
                al.add(""+s+"->"+a[i]);
            }else{
                al.add(""+s);
            }
        }
            return al;
    }
}