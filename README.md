# Custom Personalizated ArchLinux

After insalling basic ArchLinux

with this command you can check if is allready installed in your system `sudo pacman -Qsq name_conntent`

Install packeges nessesary

	sudo pacman -S alacritty code xterm kitty firefox rofi which nitrogen nodejs npm python python-pip ruby rubygems alsa-utils 
	sudo pacman -S burpsuit locate neofetch ranger 
	sudo pacman -S ttf-dejavu ttf-liberation noto-fonts noto-fonts-emoji
	
	
	

installing repos for BlackArch 

	mkdir blackarch
	cd !$
	curl -O https://blackarch.org/strap.sh
	chmod +x strap.sh
	sudo su
	./strap.sh
	
	pacman -Sy


Install Qtile and dependencies:

	sudo pacman -S qtile pacman-contrib
	sudo pacman -S noto-fonts-emoji noto-fonts 

In case of YAY:

	yay -S nerd-fonts-ubuntu-mono
	
	
or in case PARU:
instalation PARU

create repo directory

	mkdir repos
	git clone https://aur.archlinux.org/paru-bin.git
	cd paru-bin
	makepkg -si

after finish installeting PARU

	paru -S nerd-fonts-ubuntu-mono
	
next:

	pip install psutil
	
if missed this:

	sudo pacman -S python-pip


Clone this repository and copy my configs:

	git clone https://github.com/antoniosarosi/dotfiles.git
	cp -r dotfiles/.config/qtile ~/.config







--------------------------------------------------


......

sudo pacman -S qtile pacman-contrib

yay or paru -S nerd-fonts-ubuntu-mono



		if yay then: pip install psutil


<clipboard-copy> element
	

# Copy to clipboard [![Build Status](https://travis-ci.org/sudodoki/copy-to-clipboard.svg?branch=master)](https://travis-ci.org/sudodoki/copy-to-clipboard)

Simple module exposing `copy` function that will try to use [execCommand](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand#) with fallback to IE-specific `clipboardData` interface and finally, resort to usual `prompt` with proper text content and message.

# Example

```js
import copy from 'copy-to-clipboard';

copy('Text');

// Copy with options
copy('Text', {
  debug: true,
  message: 'Press #{key} to copy',
});
```

# API

`copy(text: string, options: object): boolean` &mdash; tries to copy text to clipboard. Returns `true` if no additional keystrokes were required from user (so, `execCommand`, IE's `clipboardData` worked) or `false`.

|Value |Default |Notes|
|------|--------|-----|
|options.debug  |false| `Boolean`. Optional. Enable output to console. |
|options.message|Copy to clipboard: `#{key}`, Enter| `String`. Optional. Prompt message. `*` |
|options.format|"text/html"| `String`. Optional. Set the MIME type of what you want to copy as. Use `text/html` to copy as HTML, `text/plain` to avoid inherited styles showing when pasted into rich text editor. |
|options.onCopy|null| `function onCopy(clipboardData: object): void`. Optional. Receives the clipboardData element for adding custom behavior such as additional formats |

`*` all occurrences of `#{key}` are replaced with `⌘+C` for macOS/iOS users, and `Ctrl+C` otherwise.

# [Browser support](http://caniuse.com/#feat=document-execcommand)

Works everywhere where `prompt`* is available. Works best (i.e. without additional keystrokes) in Chrome, FF, Safari 10+, and, supposedly, IE/Edge.

Note: **does not work on some older iOS devices.**  
`*` – even though **Safari 8** has `prompt`, you cannot specify prefilled content for prompt modal – thus it **doesn't work** as expected.

# Installation

+ Can be used as npm package and then leveraged using commonjs bundler/loader:
```
npm i --save copy-to-clipboard
```
+ Can be utilized using [wzrd.in](https://wzrd.in/). Add following script to your page:
```html
<script src="https://wzrd.in/standalone/copy-to-clipboard@latest" async></script>
```
You will have `window.copyToClipboard` exposed for you to use.

# UI components based on this package:
+ [react-copy-to-clipboard](https://github.com/nkbt/react-copy-to-clipboard)
+ [copy-button](https://github.com/sudodoki/copy-button)

# See also:
+ [clipboard-copy](https://github.com/feross/clipboard-copy) by [@feross](https://github.com/feross)
+ [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand#Browser_Compatibility)
+ [April 2015 update on Cut and Copy Commands](http://updates.html5rocks.com/2015/04/cut-and-copy-commands)

# Running Tests
This project has some automated tests, that will run using [nightwatch](nightwatchjs.org) on top of [selenium](http://www.seleniumhq.org/).

```
npm i
npm test
```
# Typescript
This library has built-in Typescript definitions.

```
import * as copy from 'copy-to-clipboard';
```
