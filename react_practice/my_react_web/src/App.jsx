const num = [1, 2, 3, 4, 5, 6, 7, 8, 9];

function App() {
  return (
    <div style={{ display: "flex" }}>
      {num.map(
        (n) =>
          n >= 2 &&
          n !== 5 && (
            <div
              style={{
                padding: 10,
                color: n % 2 === 0 ? "black" : "blue",
              }}
              key={n}
            >
              {num.map((m) => (
                <div key={`${n}-${m}`}>
                  {n}x{m}={n * m}
                </div>
              ))}
            </div>
          )
      )}
    </div>
  );
}

export default App;