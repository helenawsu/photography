import { writable } from 'svelte/store';

export const show_full_img = writable(false);
export const show_start_msg = writable(true);
export const focused_img = writable({
  alt: 'string',
  src: 'string',
  original_path: 'string',
  tags: ['string'],
  time: ['string', 0],
  hv: true,
  rating: 0,
});

export const current_scroll_position = writable(0);
export const filtered_image = writable([{
  alt: 'string',
  src: 'string',
  original_path: 'string',
  tags: ['string'],
  time: ['string', 0],
  hv: true,
  rating: 0,
}]);
