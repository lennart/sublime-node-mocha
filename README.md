# sublime-node-mocha

SublimeText 2 Snippets and Syntax Highlighter for the testing framework [__mocha__](http://github.com/visionmedia/mocha). Although the name implies node.js, __mocha__ works as well in the browser.

__WARNING__: this is an early release of, expect [bugs…](https://github.com/lennart/sublime-node-mocha/issues)
# Installation

```shell
git clone git://github.com/lennart/sublime-node-mocha.git <path-to-your-packages-folder>/Mocha
```

Or use the [Sublime Text 2 Package Manager](http://wbond.net/sublime_packages/package_control)


# Usage

Given your tests lie within the `test` folder relative to the root of your project, __sublime-node-mocha__ will automatically use an enhanced javascript
syntax to highlight __describe__ and __it__ blocks as well as specific calls like `done()` or `beforeEach(...)`.

Within a test file you can use the following snippets:

* `it<tab>` => `it("should behave like", function() { ... });`

* `ait<tab>` => `it("should behave like", function(done) { ...; done(); });`

* `describe<tab>` => `describe("a trait", function() { ...});`

more might follow…