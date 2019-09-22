#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>

#include <cmath>

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  int n;
  std::cin >> n;
  int num = 0;
  vector<int> nums;
  for (int i = max(0, n-81); i < n+1; i++) {
    int j = i+0;
    int s = 0;
    while (j != 0) {
      s += j % 10;
      j /= 10;
    }
    if (i+s == n) {
      num += 1;
      nums.push_back(i);
    }
  }
  std::cout << num << "\n";
  if (not nums.empty()) {
    std::cout << nums[0];
    for (int i = 1; i < nums.size(); i++) {
      std::cout << " " << nums[i];
    }
    std::cout << "\n";
  }
  return 0;
}
