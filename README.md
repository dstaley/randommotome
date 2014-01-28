# Random Moto Me!

I'm having a hard time designing my Moto X, so I thought it'd be neat to be able to see random color combinations.

## Routes
* `/` runs the Ember frontend. You can view this live at [randommoto.me](http://randommoto.me).
* `/random` redirects to a random Moto X image.
* `/random.json` returns a JSON response in the following format:

```json
{
  "accent": "OP100027", 
  "back": "OP100016", 
  "front": "white", 
  "url": "/img/white/OP100016/OP100027/82PA00000043.png", 
  "wallpaper": "82PA00000043"
}
```

* `/img/<front>/<back>/<accent>/<wallpaper>.png` returns a Moto X image with the specified color choices.