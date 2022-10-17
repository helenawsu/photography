import { writable } from 'svelte/store';

export const show_full_img = writable(false);
export const focused_img = writable({
  alt: 'string',
  src: 'string',
  original_path: 'string',
  tags: ['string'],
  time: ['string', 0],
  hv: true,
});

export const current_scroll_position = writable(0);
