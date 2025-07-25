import { useEffect, useState } from "react";

type TeeTime = {
  id: number;
  time: string;
  discountedPrice: number;
};

type Course = {
  id: number;
  name: string;
  location: string;
  availableTeeTimes: TeeTime[];
};

function App() {
  const [query, setQuery] = useState<string>("");
  const [results, setResults] = useState<Course[]>([]);
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    if (query.length < 3) return;

    const timeout = setTimeout(() => {
      setLoading(true);
      fetch(`http://127.0.0.1:8000/api/search?query=${query}`)
        .then((res) => res.json())
        .then((data) => setResults(data))
        .finally(() => setLoading(false));
    }, 400);

    return () => clearTimeout(timeout);
  }, [query]);

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">SpareTee</h1>
      <input
        type="text"
        className="w-full border px-3 py-2 rounded mb-4"
        placeholder="Search Chicago-area courses..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      {loading && <p>Loading...</p>}

      <div className="space-y-4">
        {results.map((course) => (
          <div key={course.id} className="border p-4 rounded shadow-sm">
            <h2 className="text-xl font-semibold">{course.name}</h2>
            <p className="text-sm text-gray-600">{course.location}</p>
            {course.availableTeeTimes.length > 0 ? (
              <ul className="mt-2 space-y-1">
                {course.availableTeeTimes.map((tee) => (
                  <li key={tee.id} className="flex justify-between items-center">
                    <span>{tee.time}</span>
                    <span className="font-medium">${tee.discountedPrice.toFixed(2)}</span>
                    <button className="bg-green-600 text-white text-sm px-3 py-1 rounded">Book</button>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-sm text-red-600 mt-2">
                No discounted tee times in next 30 minutes
              </p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
