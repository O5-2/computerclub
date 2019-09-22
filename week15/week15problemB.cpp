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

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  int n;
  int k;
  std::cin >> n >> k;
  int stash = 0;
  int given = 0;
  int gains[n];
  for (int i = 0; i < n; i++) {
    std::cin >> gains[i];
    stash += gains[i];
    given += std::min(8, stash);
    stash -= std::min(8, stash);
    if (given >= k) {
      std::cout << i+1 << "\n";
      break;
    }
  }
  if (given < k)
    std::cout << "-1\n";
  return 0;
}
