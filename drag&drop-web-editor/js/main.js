var editor = grapesjs.init({
    // height: '50%',
    // showOffsets: 1,
    container: '#gjs',
    noticeOnUnload: 0,
    storageManager: false,//{autoload: 0},
    fromElement: true,
    width:"auto",
    plugins: ['grapesjs-preset-webpage','gjs-preset-newsletter','grapesjs-navbar'],//'gjs-blocks-basic', 'gjs-plugin-actions',
    pluginsOpts: {
        'grapesjs-preset-webpage': {
            // options
          },
          'grapesjs-navbar':{

          },
          'gjs-preset-newsletter': {
            modalTitleImport: 'Import template',
            // ... other options
          }
        // 'gjs-plugin-actions': {},
        // 'gjs-blocks-basic': {
        //     flexGrid: 1
        // },
    },
//     blockManager: {
// appendTo: '#blocks',
blocks: []
// },
});
window.editor = editor;