<script>
  import { exioCheckbox } from 'exio/svelte';
  import { photos, other_collapsible_tags, misc_tags } from './create_img.js';
  import { show_start_msg, filtered_image } from './store.js';

  /** @type {string}*/
  let featured_tag = "Berkeley Botanical Garden";
  /** @type {string[]}*/
  export let filtered_tags = [];
  let feature = true;

  let collapsible_tags = other_collapsible_tags;
  export let no_img_found = false;
  

  /**
   * @type {string | any[]}
   */
   export let filtered_img = [];

  /** @param {number} num */
  function collapse(num) {
    show_start_msg.set(false);
    let bo = collapsible_tags[num].collapsed;
    collapsible_tags = [
      ...collapsible_tags.slice(0, num),
      {
        name: collapsible_tags[num].name,
        collapsed: !bo,
        tags: collapsible_tags[num].tags,
      },
      ...collapsible_tags.slice(num + 1, collapsible_tags.length),
    ];
  }

  /** @returns { { alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; rating: number;}[]}
   * @param {string[]} filtered_tags_param */
  function refresh(filtered_tags_param) {
    if (filtered_tags_param.includes('All')) {
      filtered_img = photos;
      console.log(filtered_img);
      return sortOnRating(filtered_img);
    }
    if (filtered_tags_param.length === 0) {
      filtered_img = [
        {
          alt: '',
          src: '',
          original_path: '',
          tags: [''],
          time: [''],
          hv: true,
          rating: 0,
        },
      ];
    } else {
      filtered_img = sortOnRating(photos.filter((photo) =>
        filtered_tags.every((tag) => photo.tags.includes(tag))
      ));
      // @ts-ignore
      filtered_image.update(n => filtered_img);
    }
    no_img_found = filtered_img.length === 0 && filtered_tags_param.length > 0;

    return sortOnRating(filtered_img);
  }

  /**
   * @param {string[]} filtered_tags
   */
  /**
   * @type {{ alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; rating:number}[]}
   */
  $: filtered_img = refresh(filtered_tags);
 // @ts-ignore
  /**@returns { { alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; rating: number;}[]}
   * @param { { alt: string; src: string; original_path: string;
   * tags: string[]; time: (string | number)[]; hv: boolean; rating: number;}[] } unsorted
   */
  function sortOnRating(unsorted) {
    let sorted = unsorted.map((img) => ({
      ...img,
      rating: img.rating + Math.random() / 10.0,
    }));
    sorted.sort(function (a, b) {
      return b.rating - a.rating;
    });
    filtered_image.update(n => sorted);
    return sorted;
  }
  window.onload = function() {
    if (feature) {
      filtered_tags = [featured_tag];
    }
    feature = false;
    refresh(filtered_tags);
};
</script>

<div class="flex-container" style="position: relative; top: 0px;">
  {#each misc_tags as misc_tag, index}
    <div style="" class="flex-items tag_groups">
      {#if index===0}
      <label style="padding-left: 10px; padding-right: 10px">
        <span>Featured: {misc_tag}</span>
        <input
          class="checkbox-format"
          type="checkbox"
          use:exioCheckbox
          name="filtered tags"
          value={misc_tag}
          checked
          bind:group={filtered_tags}

        />
      </label>
        {:else}
      <label style="padding-left: 10px; padding-right: 10px">
        <span>{misc_tag}</span>
        <input
          class="checkbox-format"
          type="checkbox"
          use:exioCheckbox
          bind:group={filtered_tags}
          name="filtered tags"
          value={misc_tag}
        />
        
      </label>
      {/if}
    </div>
  {/each}
</div>

<div class="flex-container">
  {#each collapsible_tags as tag_group, num}
    <div class="tag_groups" style="">
      <div class="flex-items">
        <button on:click={() => collapse(num)}>
          {#if tag_group.collapsed}
            <div class="triangle-right" />
          {:else}
            <div class="triangle-down" />
          {/if}
          <h4>{tag_group.name}</h4></button
        >
      </div>
      {#each tag_group.tags.slice(0, !tag_group.collapsed ? tag_group.tags.length : 2) as a_tag_, index}
        <div class="flex-items">
          <label>
            <input
              class="checkbox-format"
              type="checkbox"
              use:exioCheckbox
              bind:group={filtered_tags}
              name="filtered tags"
              value={tag_group.tags[index]}
            />
            <span>
              {tag_group.tags[index]}
            </span>
          </label>
        </div>
        <div />
      {/each}
    </div>
  {/each}
</div>

<style>
  h4 {
    font-family: 'Inknut Antiqua', serif;
    font-size: 1.5rem;
    color: #d9dbca;
    margin: 0;
    padding: 0;
    padding-left: 0px;
    padding-right: 10px;
    line-height: normal;
    display: inline;
    height: 100%;
    /* border-left: #a89732 5px solid; */
  }
  @media screen and (max-width: 600px) {
    h4 {
      /* line-height: 0; */
      max-width: 100%;
      font-size: 1.25rem;
      /* vertical-align:-webkit-baseline-middle; */
    }
  }

  input {
    vertical-align: middle;
    position: relative;
    margin-right: 20px;
  }
  @media screen and (max-width: 600px) {
    input {
      margin-right: 10px;
    }
  }
  button {
    background-color: #0f0f19;
    font-family: 'Inknut Antiqua', serif;
    border: none;
    margin: 0px;
    padding: 0px;
    color: white;
    padding-left: 5px;
    padding-top: 5px;
    padding-bottom: 5px;
  }

  button:hover {
    background-color: #464d4f;
  }
  button:active {
    background-color: #464d4f;
  }

  span {
    vertical-align: middle;
    position: relative;
    bottom: 3px;
  }

  .checkbox-format {
    display: inline-flex;
    border-color: #919cbf;
    vertical-align: -webkit-baseline-middle;
    /* margin:0; */
    margin-right: 0;
    padding: 0;
  }
  .checkbox-format:hover {
    --exio-hover-border-color: white;
  }

  @media screen and (max-width: 600px) {
  }

  label {
    font-family: 'Texturina', serif;
    font-size: 1.5rem;
    /* background-image: linear-gradient
    (to left, rgba(255, 217, 0, 0.43) , rgba(145, 156, 191, 0.43)); */
    margin-left: 0px;
    margin-right: 0px;
    padding-right: 0px;
    padding-left: 15px;
    color: #d9dbca;
    /* display: inline-flex; */
    /* border-left: solid #a89732 0.5px; */
    display: block;
  }
  @media screen and (max-width: 600px) {
    label {
      font-size: 1.25rem;
      padding-left: 5px;
      margin-left: 5px;
    }
  }

  .flex-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-bottom: 0px;
  }
  @media screen and (max-width: 600px) {
    .flex-container {
      max-width: 100%;
      flex-wrap: wrap;
    }
  }
  .flex-items {
    padding: 10px; /* sthis */
    align-items: center;
    display: flex;
    flex-direction: row;
  }
  @media screen and (max-width: 600px) {
    .flex-items {
      padding: 5px;
    }
  }
  .tag_groups {
    display: flex;
    background-color: #232421;
    padding: 5px;
    margin: 5px;
  }
  @media screen and (max-width: 600px) {
    .tag_groups {
      max-width: fit-content;
      padding: 5px;
      margin: 5px;
      flex-wrap: wrap;
      display: inline-block;
    }
  }
  .triangle-down {
    display: inline-flex;
    margin-left: auto;
    margin-right: auto;
    width: 0;
    height: 0;
    border-bottom: 20px solid transparent;
    /* border-right:5px solid transparent; */
    border-top: 20px solid transparent;
    border-left: 25px solid #ffe54d;
    margin: 0;
    padding: 0;
    margin-bottom: 10px;
    vertical-align: middle;
  }
  @media screen and (max-width: 600px) {
    .triangle-down {
      border-left: 20px solid transparent;
      border-bottom: 0px solid transparent;
      border-right: 20px solid transparent;
      border-top: 30px solid #ffe54d;
    }
  }
  .triangle-right {
    display: inline-flex;
    margin-left: auto;
    margin-right: auto;
    width: 0;
    height: 0;
    border-bottom: 20px solid transparent;
    /* border-right:5px solid transparent; */
    border-top: 20px solid transparent;
    border-left: 15px solid #a89732;
    margin: 0;
    padding: 0;
    margin-right: 10px;
    vertical-align: sub;
    transform: translateY(7px);
  }
  @media screen and (max-width: 600px) {
    .triangle-right {
      margin-right: 10px;
      border-bottom: 20px solid transparent;
      border-right: 0px solid transparent;
      border-top: 20px solid transparent;
      border-left: 30px solid #a89732;
    }
  }
</style>
