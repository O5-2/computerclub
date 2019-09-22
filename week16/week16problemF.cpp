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
#include <iomanip>

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  string s;
  std::cin >> s;
  string t;
  std::cin >> t;
  bool possible = true;
  string vowels = "aeiou";
  if (s.length() == t.length()) {
    for (int i = 0; i < s.length(); i++) {
      if ((vowels.find(s[i]) != string::npos) ^ (vowels.find(t[i]) != string::npos))
	possible = false;
    }
  } else
    possible = false;
  if (possible)
    std::cout << "Yes\n";
  else
    std::cout << "No\n";
  return 0;
}
