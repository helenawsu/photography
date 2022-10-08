<script>
  import { exioCheckbox } from 'exio/svelte';
  import { photos, other_collapsible_tags, misc_tags } from './create_img.js';

  /**
   * @type {string[]}
   */
  export let filtered_tags = [];

  let collapsible_tags = other_collapsible_tags;
  export let show_start_message = true;
  export let no_img_found = false;

  export let filtered_img = [];

  /**
   * @param {number} num
   */
  function collapse(num) {
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

  /**
   * @returns { { alt: string; src: string; original_path: string; tags: string[]; time: (string | number)[]; hv: boolean; }[]}
   * @param {string[]} filtered_tags_param
   */
  function refresh(filtered_tags_param) {
    filtered_img = [];
    if (filtered_tags_param.includes('All')) {
      filtered_img = photos;
      return filtered_img;
    }
    for (var m = 0; m < photos.length; m++) {
      var add;
      if (filtered_tags_param.length > 0) {
        add = true;
        show_start_message = false;
      } else {
        show_start_message = true;
        add = false;
      }

      for (var n = 0; n < filtered_tags_param.length; n++) {
        if (!photos[m].tags.includes(filtered_tags_param[n])) {
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

    return filtered_img;
  }

  /**
   * @param {string[]} filtered_tags
   */
  /**
   * @type {{ alt: string; src: string; original_path: string; tags: string[]; time: (string | number)[]; hv: boolean; }[]}
   */
  $: filtered_img = refresh(filtered_tags);
</script>

<div class="flex-container" style="position: relative; top: 0px;">
  {#each misc_tags as misc_tag}
    <div class="flex-items">
      <label>
        {misc_tag}
        <input
          class="checkbox-format"
          type="checkbox"
          use:exioCheckbox
          bind:group={filtered_tags}
          name="filtered tags"
          value={misc_tag}
        />
      </label>
    </div>
  {/each}
</div>

<div class="flex-container">
  {#each collapsible_tags as tag_group, num}
    {#if tag_group.collapsed}
      <h4>{tag_group.name}</h4>
      <div class="flex-items">
        {#each tag_group.tags.slice(0, 2) as a_tag, index}
          <label>
            {tag_group.tags[index]}
            <input
              class="checkbox-format"
              type="checkbox"
              use:exioCheckbox
              bind:group={filtered_tags}
              name="filtered tags"
              value={tag_group.tags[index]}
            />
          </label>
        {/each}
      </div>
      <div>
        <button on:click={() => collapse(num)}>More</button>
      </div>
    {:else}
      <h4>{tag_group.name}</h4>
      <div class="flex-items">
        {#each tag_group.tags as a_tag}
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
        {/each}
      </div>
      <div>
        <button on:click={() => collapse(num)}>Less</button>
      </div>
    {/if}
  {/each}
</div>

<style>
  h4 {
    font-family: 'Inknut Antiqua', serif;
    font-size: 1.5rem;
    color: white;
    padding-left: 10px;
    vertical-align: middle;
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

  label {
    font-family: 'Texturina', serif;
    font-size: 1.5rem;
    /* background-image: linear-gradient(to left, rgba(255, 217, 0, 0.43) , rgba(145, 156, 191, 0.43)); */
    margin-left: 0px;
    padding-right: 0px;
    padding-left: 15px;
    display: block;
    color: #d9dbca;
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
    margin-bottom: 0px;
  }

  .flex-items {
    padding: 10px; /* this */
  }
</style>
