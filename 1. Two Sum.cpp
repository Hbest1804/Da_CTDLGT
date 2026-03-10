
#include<iostream>
#include<unordered_map>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for(int i=0; i<nums.size();i++){
            int needs = target- nums[i];
            if(mp.count(needs)){
                return {mp[needs],i};
            }
            mp[nums[i]] =i;
            
        }
        return {};
    }
};