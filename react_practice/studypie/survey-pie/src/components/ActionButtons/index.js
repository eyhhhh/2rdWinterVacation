import { useNavigate } from 'react-router-dom';

function ActionButtons({ questionsLength, step }) {
  const navigate = useNavigate();
  const isLast = questionsLength - 1 === step;
  return (
    <div>
      {step === 0 || (
        <button
          onClick={() => {
            navigate(`${step - 1}`); // 문자열로 변환
          }}
        >
          이전
        </button>
      )}
      {isLast ? (
        <button
          onClick={() => {
            navigate('/done');
          }}
        >
          제출
        </button>
      ) : (
        <button
          onClick={() => {
            navigate(`${step + 1}`); // 문자열로 변환
          }}
        >
          다음
        </button>
      )}
    </div>
  );
}

export default ActionButtons;
