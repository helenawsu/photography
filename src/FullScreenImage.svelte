<script>
  import {
    focused_img,
    show_full_img,
    current_scroll_position,
  } from './store.js';

  let scroll = false;
  /**
   * @type {number}
   */
  let y;

  /**
   * @type {number}
   */
  let c_scroll_position;

  /**
   * @type {{ alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; }}
   */
  let fs_img;
  focused_img.subscribe((value) => {
    fs_img = value;
  });
  current_scroll_position.subscribe((value) => {
    c_scroll_position = value;
  });
  function exitFullScreen() {
    scroll = true;
    console.log('exiting');
    show_full_img.set(false);
  }
  $: show_full_img &&
    setTimeout(() => {
      console.log('is it scrolling ', scroll);

      if (scroll) {
        window.scrollTo(0, c_scroll_position);
        console.log('scrolling', current_scroll_position);
      }

      scroll = false;
    }, 3);
</script>

<div class="fullscreen">
  <h4 style=" grid-column: 3; grid-row: 1;" class="fullscreenimg description">
    {fs_img.alt}
  </h4>

  <button on:click={exitFullScreen}>EXIT</button>
  {#if fs_img.hv}
    <img
      class="fullscreenimg_big_h"
      src={fs_img.original_path}
      alt={fs_img.alt}
    />
    <img
      class="fullscreenimg_small_h stretch_h"
      src={fs_img.src}
      alt={fs_img.alt}
    />
  {:else}
    <img
      class="fullscreenimg_big_v"
      src={fs_img.original_path}
      alt={fs_img.alt}
    />
    <img
      class="fullscreenimg_small_v stretch_v"
      src={fs_img.src}
      alt={fs_img.alt}
    />
  {/if}
</div>

<style>
  h4 {
    font-family: 'Inknut Antiqua', serif;
    font-size: 1.5rem;
    color: white;
    padding-left: 10px;
    vertical-align: middle;
  }

  button {
    background-color: #0f0f19;
    border: none;
    display: inline-flex;
    grid-column: 1;
    grid-row: 1;
    height: 95vh;
    float: right;
    align-items: center;
    justify-content: center; /* center the content horizontally */
    color: #d9dbca;
    font-size: 1.25rem;
    font-family: 'Piazzolla', serif;
    margin-right: 20px;
  }
  button:hover {
    background-color: #464d4f;
  }
  .description {
    text-align: center;
    vertical-align: middle;
    align-self: center;
    padding-left: 20px;
    padding-right: 20px;
  }

  @media screen and (max-width: 600px) {
  }
  .stretch_h {
    width: 70vw;
  }
  .stretch_v {
    height: 90vh;
  }
  .fullscreen {
    display: grid;
    align-content: center;
    position: relative;
  }
  .fullscreen > .fullscreenimg_big_h {
    grid-column: 2;
    grid-row: 1;
    z-index: -1;
    max-width: 70vw;
    align-self: center;
  }
  .fullscreen > .fullscreenimg_big_v {
    grid-column: 2;
    grid-row: 1;
    z-index: -1;
    max-height: 90vh;
    align-self: center;
  }
  .fullscreen > .fullscreenimg_small_h {
    grid-column: 2;
    grid-row: 1;
    z-index: -2;
    align-self: center;
  }
  .fullscreen > .fullscreenimg_small_v {
    grid-column: 2;
    grid-row: 1;
    z-index: -2;
    align-self: center;
  }
  img {
    display: block;

    margin-left: auto;
    margin-right: auto;
  }

  @media screen and (max-width: 600px) {
    img {
      max-width: 100%;
      max-height: 25rem;
      object-fit: contain;
    }
  }
</style>
