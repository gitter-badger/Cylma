## Cylma
###### PRs are welcome!
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

### Example

##### Input
```
$ python cylma.py -i 8.8.8.8 -u Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F56.0.2924.87%20Safari%2F537.36%20OPR%2F43.0.2442.1144
```

##### Output
[Click to see](https://github.com/nig/Cylma/blob/master/data.json)


### TODOs

- [ ] Make user-friendly output on terminal
- [ ] Make URL encoding support for User-Agents
- [ ] Make multi-threaded
- [ ] Add self-documentation
- [ ] Test in Linux (Debian & Arch) systems


### Screenshot(s)

[![](https://github.com/nig/Cylma/blob/master/images/screenshot.PNG)](https://github.com/nig/Cylma/tree/master/images/)


### License

[![](http://www.wtfpl.net/wp-content/uploads/2012/12/logo-220x1601.png)](https://github.com/nig/Cylma/blob/master/LICENSE)
