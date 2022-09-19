<script>
  import { exioCheckbox } from 'exio/svelte';
  import { get } from 'svelte/store';
  import { photos, all_tags, collapse_tags } from './create_img.js';

  var show_start_message = true;
  var no_img_found = false;
  /**
   * @type {string | any[]}
   */
  var filtered_tags = [];
  /**
   * @type {any[]}
   */
  var filtered_img = [];

  let col_exp = true;
  function collapse() {
    col_exp  = !col_exp;
  }
  /**
   * @param {string | any[]} filtered_tags
   */
  function refresh(filtered_tags) {
    filtered_img = [];
    if (filtered_tags.includes('All')) {
      filtered_img = photos;
      return filtered_img;
    }
    for (var m = 0; m < photos.length; m++) {
      var add;
      if (filtered_tags.length > 0) {
        add = true;
        show_start_message = false;
      } else {
        show_start_message = true;
        add = false;
      }

      for (var n = 0; n < filtered_tags.length; n++) {
        if (!photos[m].tags.includes(filtered_tags[n])) {
          add = false;
        }
      }
      if (add) {
        filtered_img.push(photos[m]);
      }
    }
    if (filtered_img.length == 0 && !show_start_message) {
      no_img_found = true;
    } else {
      no_img_found = false;
    }

    console.log(filtered_img);
    return filtered_img;
  }
  $: filtered_img = refresh(filtered_tags);
</script>

<main style="margin: 0px, padding: 0px">
  <p class="lastupdatetime">This page was last updated on Sep 18, 2022.</p>
  <h2 style="padding-bottom: 10px">HELENA SU PHOTOGRAPHY</h2>

  <br />

  <div class="flex-container">
    {#each Object.entries(collapse_tags) as [key, value]}
      {#if col_exp}
      <div class="flex-items">
        <label>
          <p>{key}</p>
          {value[0]}

          <input
            class="checkbox-format"
            type="checkbox"
            use:exioCheckbox
            bind:group={filtered_tags}
            name="filtered tags"
            value={value[0]}
          />
        </label>
      </div>
      <button on:click={collapse}>More</button>

      {:else}
      <p>{key}</p>

      <div class="flex-items">
        {#each value as single_tag}
        <label>
          {single_tag}

          <input
            class="checkbox-format"
            type="checkbox"
            use:exioCheckbox
            bind:group={filtered_tags}
            name="filtered tags"
            value={single_tag}
          />
        </label>
        {/each}
      </div>
      <button on:click={collapse}>Less</button>

      {/if}

    {/each}

  </div>

  <div class="flex-container">
    {#each all_tags as a_tag}
      <div class="flex-items">
        <label>
          {a_tag}

          <input
            class="checkbox-format"
            type="checkbox"
            use:exioCheckbox
            bind:group={filtered_tags}
            name="filtered tags"
            value={a_tag}
          />
        </label>
      </div>
    {/each}
  </div>

  {#if show_start_message}
    <p>please select as least one tag.</p>
  {/if}

  {#if no_img_found}
    <p>No photos are found!!!!</p>
  {/if}

  <div class="flex-container">
    {#each filtered_img as a_photo}
      <!-- svelte-ignore a11y-missing-attribute -->
      <div class="flex-items">
        {#if a_photo.hv}
          <img {...a_photo} style="width:600px" />
        {:else}
          <img {...a_photo} style="height:500px" />
        {/if}
      </div>
    {/each}
  </div>
</main>

<style>
  main {
    /* text-align: center; */
    padding: 1em;
    /* max-width: 240px; */
    /* background-color: beige; */
  }
  .lastupdatetime {
    color: #464d4f;
    margin-left: 10px;
    margin-top: 0px;
    text-align: right;
    /* line-height: 1rem; */
    /* font-family: 'Didact Gothic', sans-serif; */
  }

  @media screen and (max-width: 600px) {
    .lastupdatetime {
      font-size: 1rem;
      text-align: center;
      /* width:fit-content; */
    }
  }

  /* h1 {
    color: #ff3e00;
    font-family: 'Bodoni Moda', serif;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  } */
  h2 {
    font-family: 'Hina Mincho', serif;
    letter-spacing: 3px;
    font-size: 4rem;
    margin: 0px;
    margin-left: 10px;
    text-align: left;
    color: #464d4f;
    font-stretch: condensed;
  }

  @media screen and (max-width: 600px) {
    h2 {
      font-size: 2.25rem;
      text-align: center;
    }
  }

  /* h3{
    font-family: 'Aboreto', cursive;
    font-size: 1.5rem;
  }
  h4{
    font-family: 'Fraunces', serif;
    font-size: 1.5rem;
  } */
  p {
    font-family: 'Piazzolla', serif;
    color: #d9dbca;
    font-size: 1.25rem;
    margin: 10px;
  }
  .checkbox-format {
    display: inline-flex;
    border-color: #919cbf;


  }
  .checkbox-format:hover {
    --exio-hover-border-color: white;


  }



  @media screen and (max-width: 600px) {
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

  label {
    font-family: 'Texturina', serif;
    font-size: 1.5rem;
    /* background-image: linear-gradient(to left, rgba(255, 217, 0, 0.43) , rgba(145, 156, 191, 0.43)); */
    margin-left: 0px;
    padding-right: 0px;
    padding-left: 15px;

    display: block;
    color: #d9dbca;
    /* border-right: solid #919cbf 0.5px; */

    /* border-bottom: solid #919cbf 0.5px; */

    border-left: solid #ffff00 0.5px;
  }
  @media screen and (max-width: 600px) {
    label {
      font-size: 1.25rem;
    }
  }

  .flex-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }

  .flex-items {
    padding: 10px; /* this */
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
