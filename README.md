## Cylma
###### PRs are welcome!

[![Join the chat at https://gitter.im/Cylma/Lobby](https://badges.gitter.im/Cylma/Lobby.svg)](https://gitter.im/Cylma/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![](https://img.shields.io/badge/Say%20Thanks!-🦉-1EAEDB.svg)](https://saythanks.io/to/nig)

Cylma is a tool for information gathering from User-Agent or IP address.
It uses following APIs:
- [IP-API](http://ip-api.com/)
- [User-Agent API](http://useragentapi.com/)
- [Shodan API](http://shodan.io/)


### Usage

```
$ python(3) cylma.py <options>
```
###### Don't forget to change Shodan & User-Agent API keys


### Testing

```
cd tests/ && pytest -vv
```


### Example

##### Input
```
$ python cylma.py -i 8.8.8.8 -u "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
```

##### Output
[Click to see](https://github.com/nig/Cylma/blob/master/data.json)


### TODOs

- [x] ~~Make URL encoding support for User-Agents~~
- [x] ~~Add unit-tests~~
- [x] ~~Make user-friendly output on terminal~~
- [ ] Re-write with OOP
- [ ] Make multi-threaded
- [ ] Test in Linux (Debian & Arch) systems


### Screenshot(s)

[![](https://github.com/nig/Cylma/blob/master/images/screenshot.PNG)](https://github.com/nig/Cylma/tree/master/images/)
[![](https://github.com/nig/Cylma/blob/master/images/screenshot2.PNG)](https://github.com/nig/Cylma/tree/master/images/)


### License

[![](http://www.wtfpl.net/wp-content/uploads/2012/12/logo-220x1601.png)](https://github.com/nig/Cylma/blob/master/LICENSE)
