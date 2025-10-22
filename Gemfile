source "https://rubygems.org"

# GitHub Pages stack (includes Jekyll + plugins it supports)
gem "github-pages", group: :jekyll_plugins

# Local admin GUI (enabled only via _config.dev.yml when you serve locally)
gem "jekyll-admin", group: :jekyll_plugins

# Ruby 3.4 compatibility for Jekyll 3.x
gem "csv"                 # Ruby 3.4 no longer ships csv by default
gem "webrick", "~> 1.9"   # required to run `jekyll serve` on Ruby 3+
gem "bigdecimal"   # <-- this is the one that fixes the new error