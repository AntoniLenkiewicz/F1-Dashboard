import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className = "nav-bar">
            <div className = "flex mt-5 ml-5 w-full">
                <Link to='/'>F1STATS</Link>
            </div>
            <div className = "flex m-5 gap-5">
                <Link to='/time'>TIME</Link>
                <Link to='/gpresults'>RESULTS</Link>
            </div>
      </nav>
    );
}


export default Navbar;