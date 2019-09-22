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
  string password;
  cin >> password;
  int n;
  cin >> n;
  string word;
  bool firstPasschar = false;
  bool secondPasschar = false;
  bool bothPasschars = false;
  for (int i = 0; i < n; i++) {
    cin >> word;
    if (word == password)
      bothPasschars = true;
    if (word[1] == password[0])
      firstPasschar = true;
    if (word[0] == password[1])
      secondPasschar = true;
  }
  if (bothPasschars or (firstPasschar and secondPasschar))
    std::cout << "YES\n";
  else
    std::cout << "NO\n";
  return 0;
}
