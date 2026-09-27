# ErrorText

元のフォルダ: `src/components/ErrorText/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: ErrorText.tsx -->
````tsx
import type { ComponentProps } from 'react';

export type ErrorTextProps = ComponentProps<'p'>;

export const ErrorText = (props: ErrorTextProps) => {
  const { children, className, ...rest } = props;

  return (
    <p className={`text-dns-16N-130 text-error-1 ${className ?? ''}`} {...rest}>
      {children}
    </p>
  );
};
````

<!-- file: index.ts -->
````ts
export { ErrorText } from './ErrorText';
````
