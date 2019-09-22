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
#include <iomanip>

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  int q;
  std::cin >> q;
  for (int i = 0; i < q; i++) {
    int n;
    std::cin >> n;
    string s;
    std::cin >> s;
    if (s.length() % 2 == 1) {
      std::cout << "YES\n2\n" << s.substr(0, (n-1)/2) << " " << s.substr((n-1)/2, s.length()) << "\n";
    } else if (s.length() != 2) {
      std::cout << "YES\n2\n" << s.substr(0, (n-2)/2) << " " << s.substr((n-2)/2, s.length()) << "\n";
    } else if (s[0] < s[1]) {
      std::cout << "YES\n2\n" << s[0] << " " << s[1] << "\n";
    } else
      std::cout << "NO\n";
  }
  return 0;
}
