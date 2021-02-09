# Working Web Scraping with JS
## Request

The Request interface of the Fetch API represents a resource request.

You can create a new Request object using the Request() constructor, but you are more likely to encounter a Request object being returned as the result of another API operation, such as a service worker FetchEvent.request.

## Task 

### 0. Readme
Write a script that reads and prints the content of a file.
    - The first argument is the file path
    - The content of the file must be read in utf-8
    - If an error occurred during the reading, print the error object

```Bash

[victorz94@DESKTOP-1U2AUK9 0x14-javascript-web_scraping]$ cat cisfun
C is super fun!
[victorz94@DESKTOP-1U2AUK9 0x14-javascript-web_scraping]$ ./0-readme.js cisfun
C is super fun!

[victorz94@DESKTOP-1U2AUK9 0x14-javascript-web_scraping]$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
[victorz94@DESKTOP-1U2AUK9 0x14-javascript-web_scraping]$ 

```
