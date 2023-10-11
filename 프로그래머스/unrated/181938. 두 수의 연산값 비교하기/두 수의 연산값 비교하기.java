class Solution {
    public int solution(int a, int b) {
        String result1 = String.valueOf(a)+String.valueOf(b);
        int result2 = 2*a*b;
        if ( Integer.parseInt(result1) >= result2) {
            return Integer.parseInt(result1);
        } else {
            return result2;
        }
    }
}