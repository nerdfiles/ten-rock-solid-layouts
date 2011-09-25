_base_css_bundle = (
  '_assets/css/reset.css',
  '_assets/css/type.css',
)

_base_js_bundle = (
  '_assets/js/plugins.js',
  '_assets/js/global.js',
)

MEDIA_BUNDLES = (
  ('global.css',)
      + _base_css_bundle
      + ('_assets/css/global.css',),
  ('global-ie.css',)
      + _base_css_bundle
      + ('_assets/css/global-ie.css',),
  ('global.js',)
      + _base_js_bundle,
),