# Screenshots Ripper

About
------
python script that screenshots of a website and cuts it down

Usage
------
By setting as below, it collects images and splits them.
"Webkit2png" is required.

```json:config.json
{
  "base_url"      : "http://example.com",
  "base_name"     : "hoge",
  "split_height"  : 1.414285,
  "device_widths" : [375,768,960],
  "paths"         : [
    ["top","/"],
    ["cancel","/cancel"],
    ["question","/question"]
  ]
}
```
