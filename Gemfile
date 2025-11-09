source "https://rubygems.org"

# Use the GitHub Pages stack (pins Jekyll and the allowed plugins/versions)
gem "github-pages", group: :jekyll_plugins

# ---- Local-only tooling (NOT used by GitHub Pages) ----
group :development do
  # Optional admin UI for local editing
  gem "jekyll-admin"

  # Ruby 3+ local dev helpers
  gem "webrick", "~> 1.9"   # needed for `bundle exec jekyll serve`
  gem "csv"                 # Ruby 3.4+: stdlib gem now separate
  gem "bigdecimal"          # Ruby 3.4+: stdlib gem now separate
end