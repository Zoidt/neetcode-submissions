public class Solution {
    public bool IsAnagram(string s, string t) {
        
        int size1 = s.Length;
        int size2 = t.Length;

        if (size1 != size2)
            return false;
        
        char[] first = s.ToCharArray();
        char[] second = t.ToCharArray();

        Array.Sort(first);
        Array.Sort(second);

        for(int i=0; i < size1; i++){
            if(first[i]!= second[i])
                return false;
        }

        return true;
    }
}
