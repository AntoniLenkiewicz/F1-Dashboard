import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className = "flex sticky top-0 z-10 bg-red-700 w-full justify-items-start text-gray-100 text-2xl text-bold">
            <div className = "flex mt-5 ml-5 w-full">
                <p>F1 STATS</p>
            </div>
            <div className = "flex m-5 gap-5">
                <Link to='/'>HOME</Link>
                <Link to='/time'>TIME</Link>
            </div>
      </nav>
    );
}


export default Navbar;