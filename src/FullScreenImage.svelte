<script>
  import {
    focused_img,
    show_full_img,
    current_scroll_position,
  } from './store.js';
  let scroll = false;
  /** @type {number}*/
  let c_scroll_position;
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
  <h4 style=" " class="fullscreenimg description">
    {$focused_img.alt}
  </h4>

  {#if $focused_img.hv}
    <img
      class="fullscreenimg_big_h"
      src={$focused_img.original_path}
      alt={$focused_img.alt}
    />
    <img
      class="fullscreenimg_small_h stretch_h"
      src={$focused_img.src}
      alt={$focused_img.alt}
    />
  {:else}
    <img
      class="fullscreenimg_big_v"
      src={$focused_img.original_path}
      alt={$focused_img.alt}
    />
    <img
      class="fullscreenimg_small_v stretch_v"
      src={$focused_img.src}
      alt={$focused_img.alt}
    />
  {/if}
  <button on:click={exitFullScreen}>EXIT</button>

</div>

<style>
  h4 {
    font-family: 'Inknut Antiqua', serif;
    font-size: 1.5rem;
    color: #d9dbca;
    padding-left: 10px;
    vertical-align: middle;
    grid-column: 3; grid-row: 1;
  }

  button {
    background-color: #0f0f19;
    border: none;
    display: inline-flex;
    grid-column: 1;
    grid-row: 1;
    height: 95vh;
    align-items: center;
    justify-content: center; /* center the content horizontally */
    color: #d9dbca;
    font-size: 1.25rem;
    font-family: 'Piazzolla', serif;
    margin-right: 20px;
  }
  @media screen and (max-width: 600px) {
    button{
      height: auto;
      margin: 0 auto; 
      margin-top: 10px; 

  display: block;
  width: 100vw;
    
    }
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
  @media screen and (max-width: 600px) {
    .fullscreen {
      max-width: 100vw;
      display: block;
      height:fit-content;
    }
  }
  .fullscreen > .fullscreenimg_big_h {
    grid-column: 2;
    grid-row: 1;
    z-index: -1;
    max-width: 70vw;
    align-self: center;
  }
  @media screen and (max-width: 600px) {
    .fullscreen > .fullscreenimg_big_h {
      display: none;
    }
  }
  .fullscreen > .fullscreenimg_big_v {
    grid-column: 2;
    grid-row: 1;
    z-index: -1;
    max-height: 90vh;
    align-self: center;
  }
  @media screen and (max-width: 600px) {
    .fullscreen > .fullscreenimg_big_v {
      display: none;
    }
  }
  .fullscreen > .fullscreenimg_small_h {
    grid-column: 2;
    grid-row: 1;
    z-index: -2;
    align-self: center;
  }
  @media screen and (max-width: 600px) {
    .fullscreen > .fullscreenimg_small_h {
      width: 90vw;
    }
  }
  .fullscreen > .fullscreenimg_small_v {
    grid-column: 2;
    grid-row: 1;
    z-index: -2;
    align-self: center;
  }
  @media screen and (max-width: 600px) {
    .fullscreen > .fullscreenimg_small_v {
      max-height: 60vh;
    }
  }
  img {
    display: block;

    margin-left: auto;
    margin-right: auto;
  }

  @media screen and (max-width: 600px) {
    img {
      width: 90vw;
      object-fit: contain;
      border: none;

    }
  }
</style>
