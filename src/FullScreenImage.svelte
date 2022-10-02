<p>full screen image</p>

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
    font-family: 'Tapestry', cursive;

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

  .flex-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-bottom: 0px;
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
