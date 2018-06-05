# Cisco ASA honeypot
Cymmetria Research, 2018.

https://www.cymmetria.com/



Contact: research@cymmetria.com

A low interaction honeypot for the Cisco ASA component capable of detecting CVE-2018-0101, a DoS and remote code execution vulnerability

It is released under the MIT license for the use of the community.


# Usage

```
Usage: asa_server.py [OPTIONS]

  A low interaction honeypot for the Cisco ASA component capable of
  detecting CVE-2018-0101, a DoS and remote code execution vulnerability

Options:
  -h, --host TEXT         Host to listen
  -p, --port INTEGER      Port to listen
  -i, --ike-port INTEGER  Port to listen for IKE
  -s, --enable_ssl        Enable SSL
  -c, --cert TEXT         Certificate File Path (will generate self signed
                          cert if not supplied)
  -v, --verbose           Verbose logging
  --help                  Show this message and exit.
  
  
Optional settings for hpfeeds logging:  
  --hpfserver	TEXT			hpfeeds Server
  --hpfport     INTEGER			hpfeeds Port
  --hpfident	TEXT			hpfeeds Ident
  --hpfsecret	TEXT			hpfeeds Secret
  --hofchannel	TEXT			hpfeeds Channel
  --serverid	TEXT			hpfeeds Serverid
```
The hpfeeds logging options can also be set by using the following os environment variables: HPFEEDS_SERVER, HPFEEDS_PORT, HPFEEDS_IDENT, HPFEEDS_SECRET, HPFEEDS_CHANNEL, SERVERID

See also
--------

https://cymmetria.com/blog/honeypot-cisco-asa-vulnerability/

http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-0101

Please consider trying out the MazeRunner Community Edition, the free version of our cyber deception platform.
https://community.cymmetria.com/
