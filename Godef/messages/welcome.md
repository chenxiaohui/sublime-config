# Godef

This Sublime Text 3 [golang](golang.org) plugin adds a `godef` command which
uses [godef](http://godoc.org/code.google.com/p/rog-go/exp/cmd/godef) to find
the definition under the cursor.

#### Compatible with GoSublime

You can use this plugin working with [GoSublime](https://github.com/DisposaBoy/GoSublime) because GoSublime is not support `godef`.

## Installation

The plugin assumes `godef` is present at `$GOPATH/bin/godef`. You need install `godef` first:

    go get -v code.google.com/p/rog-go/exp/cmd/godef
    
#### Sublime Package Control

If you are using [Sublime Package Control](http://wbond.net/sublime_packages/package_control) you can simply install Sublime Reader by searching for `Godef` in the package listing.

#### Manual Install

Git clone this repository and place the entire `Godef` directory into your `Packages` directory.

OSX:

    # Install the plugin
    git clone git@github.com:buaazp/Godef.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Godef

Linux:

    # Install the plugin
    git clone git@github.com:buaazp/Godef.git ~/.config/sublime-text-3/Packages/Godef
    
Windows:


	Currently not supported.


## Settings

### Configuring `GOPATH`

You need to add gopath to the setting file before using this plugin. Here's an example `Godef.sublime-settings`:

    {
        "gopath": "/Users/zippo/develop/GO"
    }

The plugin will determine `GOPATH` from either:

1. The `gopath` value from `Godef.sublime-settings`
2. The `GOPATH` environment variable


### Key Bindings

The default key of Godef is `super/ctrl+d`. Here's an example key binding:

    { "keys": ["super+d"], "command": "godef" }

You can also add these two key-binding into your keymap file to jump between the postions. Using j/k is because I use vim mode. Change them by yourself:

	{ "keys": ["super+j"], "command": "jump_forward"},
	{ "keys": ["super+k"], "command": "jump_back"},

Enjoy it!

## License

Godef is under BSD license which is in the license file.


