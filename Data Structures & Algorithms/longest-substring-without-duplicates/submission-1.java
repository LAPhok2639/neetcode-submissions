class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> seen = new HashSet<>();
        int maxLen = 0;
        int gauche = 0;

        for (int droite=0; droite<s.length(); droite++) {
            char c = s.charAt(droite);

            while (seen.contains(c)) {
            seen.remove(s.charAt(gauche));
            gauche++;
            }

        seen.add(c);

        maxLen = Math.max(maxLen, droite - gauche + 1);
        }
        return maxLen;  
    }
}
