import { Resvg } from '@resvg/resvg-js';
import { readFileSync, writeFileSync } from 'fs';

const here = new URL('.', import.meta.url);
const svg = readFileSync(new URL('post.svg', here), 'utf8');

const resvg = new Resvg(svg, {
  background: '#070C16',
  fitTo: { mode: 'width', value: 3168 },
  font: {
    defaultFontFamily: 'DejaVu Sans',
    fontFiles: [
      '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
      '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
      '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
      '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',
    ],
  },
});

const png = resvg.render().asPng();
writeFileSync(new URL('php2shell_post.png', here), png);
console.log('rendered php2shell_post.png', png.length, 'bytes');
