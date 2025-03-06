import { useNavigate } from 'react-router-dom';

import Button from '../Button';

function ActionButtons({ questionsLength, step }) {
  const navigate = useNavigate();
  const isLast = questionsLength - 1 === step;
  return (
    <div>
      {step === 0 || (
        <Button
        type = 'TERTIARY'
          onClick={() => {
            navigate(`${step - 1}`); // 문자열로 변환
          }}
        >
          이전
        </Button>
      )}
      {isLast ? (
        <Button
        type='PRIMARY'
          onClick={() => {
            navigate('/done');
          }}
        >
          제출
        </Button>
      ) : (
        <Button
        type='PRIMARY'
          onClick={() => {
            navigate(`${step + 1}`); // 문자열로 변환
          }}
        >
          다음
        </Button>
      )}
    </div>
  );
}

export default ActionButtons;
