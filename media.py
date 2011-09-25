_base_css_bundle = (
  'css/reset.css',
  'css/type.css',
)

_base_js_bundle = (
  'js/plugins.js',
  'js/global.js',
)

MEDIA_BUNDLES = (
  ('global.css',)
      + _base_css_bundle
      + ('css/global.css',),
      
  ('global-ie.css',)
      + _base_css_bundle
      + ('css/global-ie.css',),
      
  ('global.js',)
      + _base_js_bundle,
)

