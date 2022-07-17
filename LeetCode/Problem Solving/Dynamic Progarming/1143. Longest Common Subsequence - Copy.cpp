//https://leetcode.com/problems/longest-common-subsequence/class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int dp[1001][1001],m=text1.length(),n=text2.length();
        for(int i=0;i<m+1;i++)
        {
            for(int j=0;j<n+1;j++)
            {
                if(i==0||j==0)
                    dp[i][j]=0;
                else if(text1[i-1]==text2[j-1])
                    dp[i][j]=1+dp[i-1][j-1];
                else
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
