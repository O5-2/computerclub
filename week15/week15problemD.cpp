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
  std::cin >> n;
  int winners[n];
  int spectator = 3;
  bool possible = true;
  for (int i = 0; i < n; i++) {
    std::cin >> winners[i];
    if (winners[i] == spectator) {
      possible = false;
      break;
    }
    spectator = 6-spectator-winners[i];
  }
  if (possible)
    std::cout << "YES\n";
  else
    std::cout << "NO\n";
  return 0;
}
