function Info() {
  return (
    <div className="accordion" id="accordionExample">
      <form className="form-inline my-2 my-lg-0">
        <input
          className="form-control mr-sm-2"
          type="search"
          placeholder="Filter"
          aria-label="Search"
        />
        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">
          Search
        </button>
        <p></p>
      </form>
      <br></br>
      <div className="accordion-item">
        <h2 className="accordion-header">
          <button
            className="accordion-button"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseOne"
            aria-expanded="true"
            aria-controls="collapseOne"
          >
            Characters
          </button>
        </h2>
        <div
          id="collapseOne"
          className="accordion-collapse collapse show"
          data-bs-parent="#accordionExample"
        >
          <div className="accordion-body">
            <ul className="list-group">
              <li className="list-group-item">
                John
                <img
                  src="/default_profile_pic.jpg"
                  className="rounded-circle"
                  width={20}
                  height={30}
                  alt="img"
                />
              </li>
              <li className="list-group-item">
                Jane
                <img
                  src="/default_profile_pic.jpg"
                  className="rounded-circle"
                  width={20}
                  height={30}
                  alt="img"
                />
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div className="accordion-item">
        <h2 className="accordion-header">
          <button
            className="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseTwo"
            aria-expanded="false"
            aria-controls="collapseTwo"
          >
            Stats
          </button>
        </h2>
        <div
          id="collapseTwo"
          className="accordion-collapse collapse"
          data-bs-parent="#accordionExample"
        >
          <div className="accordion-body">Word count: 1000</div>
        </div>
      </div>
    </div>
  );
}

export default Info;
