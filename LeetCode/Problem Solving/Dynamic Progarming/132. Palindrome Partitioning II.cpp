//https://leetcode.com/problems/palindrome-partitioning-ii/
class Solution {
public:
    int dp[2001][2001];
    bool isPal(string s,int i,int j)
    {
        while(i<j)
        {
            if(s[i]!=s[j]) 
                return false;
            i++;
            j--;
        }
        return true;
    }
    int solve(string s,int i,int j)
    {
        if(i>=j) 
            return 0;
        if(isPal(s,i,j))
            return dp[i][j]=0;
        if(dp[i][j]!=-1)
            return dp[i][j];
        int ans=INT_MAX;
        for(int k=i;k<j;k++)
        {
            if(isPal(s,i,k))
            {
                int left,right,temp;
                if(dp[i][k]!=-1)
                    left=dp[i][k];
                else
                {
                    left=solve(s,i,k);
                    dp[i][k]=left;
                }
                if(dp[k+1][j]!=-1)
                    right=dp[k+1][j]; 
                else
                {
                    right=solve(s,k+1,j);
                    dp[k+1][j]=right;
                }
                temp=left+right+1;
                ans=min(ans,temp);
            }
        }
        return dp[i][j]=ans;
    }
    int minCut(string s) {
        memset(dp,-1,sizeof(dp));
        return solve(s,0,s.length()-1);
    }
};
